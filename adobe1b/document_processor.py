import PyPDF2
import re
import json
from typing import List, Dict, Tuple, Any
from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from datetime import datetime
import os

class DocumentProcessor:
    def __init__(self):
        """Initialize the document processor with a lightweight sentence transformer model."""
        # Using a small model to meet the 1GB constraint
        self.model = SentenceTransformer('all-MiniLM-L6-v2')  # ~90MB model
        self.section_patterns = [
            r'^[A-Z][A-Z\s]+$',  # ALL CAPS titles
            r'^\d+\.\s+[A-Z]',   # Numbered sections
            r'^[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*$',  # Title case
            r'^Chapter\s+\d+',   # Chapter headers
            r'^Section\s+\d+',   # Section headers
        ]
    
    def extract_text_from_pdf(self, pdf_path: str) -> List[Dict[str, Any]]:
        """Extract text and identify sections from a PDF document."""
        sections = []
        
        try:
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                
                for page_num, page in enumerate(pdf_reader.pages, 1):
                    text = page.extract_text()
                    if not text.strip():
                        continue
                    
                    # Split text into paragraphs
                    paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
                    
                    current_section = {
                        'document': os.path.basename(pdf_path),
                        'page_number': page_num,
                        'section_title': f"Page {page_num}",
                        'content': '',
                        'subsections': []
                    }
                    
                    for para in paragraphs:
                        # Check if paragraph is a section header
                        if self._is_section_header(para):
                            if current_section['content']:
                                sections.append(current_section)
                            
                            current_section = {
                                'document': os.path.basename(pdf_path),
                                'page_number': page_num,
                                'section_title': para.strip(),
                                'content': '',
                                'subsections': []
                            }
                        else:
                            current_section['content'] += para + '\n\n'
                    
                    if current_section['content']:
                        sections.append(current_section)
                        
        except Exception as e:
            print(f"Error processing {pdf_path}: {str(e)}")
            
        return sections
    
    def _is_section_header(self, text: str) -> bool:
        """Check if text appears to be a section header."""
        text = text.strip()
        if len(text) < 3 or len(text) > 100:
            return False
            
        for pattern in self.section_patterns:
            if re.match(pattern, text):
                return True
        return False
    
    def extract_subsections(self, section_content: str) -> List[Dict[str, Any]]:
        """Extract subsections from section content."""
        subsections = []
        
        # Split by common subsection indicators
        subsection_indicators = [
            r'\n\d+\.\s+',  # Numbered subsections
            r'\n[A-Z]\.\s+',  # Lettered subsections
            r'\n•\s+',  # Bullet points
            r'\n-\s+',  # Dashes
        ]
        
        content_parts = [section_content]
        for pattern in subsection_indicators:
            new_parts = []
            for part in content_parts:
                split_parts = re.split(pattern, part)
                new_parts.extend(split_parts)
            content_parts = new_parts
        
        for i, part in enumerate(content_parts):
            if part.strip():
                subsections.append({
                    'subsection_id': i + 1,
                    'refined_text': part.strip(),
                    'page_number_constraints': None  # Will be filled later
                })
        
        return subsections
    
    def calculate_relevance_score(self, text: str, persona: str, job: str) -> float:
        """Calculate relevance score using semantic similarity."""
        try:
            # Combine persona and job for context
            context = f"{persona}: {job}"
            
            # Encode the context and text
            context_embedding = self.model.encode([context])
            text_embedding = self.model.encode([text])
            
            # Calculate cosine similarity
            similarity = cosine_similarity(context_embedding, text_embedding)[0][0]
            
            return float(similarity)
        except Exception as e:
            print(f"Error calculating relevance: {str(e)}")
            return 0.0
    
    def rank_sections(self, sections: List[Dict], persona: str, job: str) -> List[Dict]:
        """Rank sections by relevance to persona and job."""
        for section in sections:
            # Calculate relevance for section title and content
            title_score = self.calculate_relevance_score(section['section_title'], persona, job)
            content_score = self.calculate_relevance_score(section['content'], persona, job)
            
            # Weighted score (title more important)
            section['importance_rank'] = (title_score * 0.7) + (content_score * 0.3)
            
            # Extract and rank subsections
            section['subsections'] = self.extract_subsections(section['content'])
            for subsection in section['subsections']:
                subsection_score = self.calculate_relevance_score(
                    subsection['refined_text'], persona, job
                )
                subsection['importance_rank'] = subsection_score
        
        # Sort sections by importance rank
        sections.sort(key=lambda x: x['importance_rank'], reverse=True)
        
        return sections
    
    def process_documents(self, document_paths: List[str], persona: str, job: str) -> Dict[str, Any]:
        """Main processing function that handles the entire pipeline."""
        start_time = datetime.now()
        
        # Extract sections from all documents
        all_sections = []
        for doc_path in document_paths:
            sections = self.extract_text_from_pdf(doc_path)
            all_sections.extend(sections)
        
        # Rank sections by relevance
        ranked_sections = self.rank_sections(all_sections, persona, job)
        
        # Get top section and its best subsection
        top_section = ranked_sections[0] if ranked_sections else None
        top_subsection = None
        
        if top_section and top_section['subsections']:
            # Sort subsections by importance
            top_section['subsections'].sort(key=lambda x: x['importance_rank'], reverse=True)
            top_subsection = top_section['subsections'][0]
        
        # Prepare all extracted sections
        all_extracted_sections = []
        for section in ranked_sections:
            all_extracted_sections.append({
                "document": section['document'],
                "page_number": section['page_number'],
                "section_title": section['section_title'],
                "importance_rank": section['importance_rank']
            })
        
        # Prepare all subsection analyses
        all_subsection_analyses = []
        for section in ranked_sections:
            for subsection in section['subsections']:
                all_subsection_analyses.append({
                    "document": section['document'],
                    "subsection_id": subsection['subsection_id'],
                    "refined_text": subsection['refined_text'],
                    "page_number_constraints": section['page_number'],
                    "importance_rank": subsection['importance_rank']
                })
        
        # Sort subsections by importance rank
        all_subsection_analyses.sort(key=lambda x: x['importance_rank'], reverse=True)
        
        # Prepare output
        output = {
            "metadata": {
                "input_documents": [os.path.basename(path) for path in document_paths],
                "persona": persona,
                "job_to_be_done": job,
                "processing_timestamp": start_time.isoformat()
            },
            "extracted_sections": all_extracted_sections,
            "sub_section_analyses": all_subsection_analyses
        }
        
        return output 