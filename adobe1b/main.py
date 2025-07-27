#!/usr/bin/env python3
"""
Persona-Driven Document Intelligence System
Main entry point for the application.
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path
from document_processor import DocumentProcessor

def validate_inputs(document_paths: list, persona: str, job: str) -> bool:
    """Validate input parameters."""
    if not document_paths:
        print("Error: No document paths provided")
        return False
    
    if not persona or not persona.strip():
        print("Error: Persona is required")
        return False
    
    if not job or not job.strip():
        print("Error: Job to be done is required")
        return False
    
    # Check if all documents exist
    for doc_path in document_paths:
        if not os.path.exists(doc_path):
            print(f"Error: Document not found: {doc_path}")
            return False
        if not doc_path.lower().endswith('.pdf'):
            print(f"Error: Only PDF files are supported: {doc_path}")
            return False
    
    return True

def main():
    """Main function to process documents based on persona and job."""
    parser = argparse.ArgumentParser(
        description="Persona-Driven Document Intelligence System"
    )
    parser.add_argument(
        "--documents", 
        nargs="+", 
        required=True,
        help="Paths to PDF documents to process"
    )
    parser.add_argument(
        "--persona", 
        required=True,
        help="Persona/role description (e.g., 'Investment Analyst')"
    )
    parser.add_argument(
        "--job", 
        required=True,
        help="Job to be done (e.g., 'Analyze revenue trends')"
    )
    parser.add_argument(
        "--output", 
        default="challenge1b_output.json",
        help="Output JSON file path (default: challenge1b_output.json)"
    )
    parser.add_argument(
        "--verbose", 
        action="store_true",
        help="Enable verbose output"
    )
    
    args = parser.parse_args()
    
    # Validate inputs
    if not validate_inputs(args.documents, args.persona, args.job):
        sys.exit(1)
    
    if args.verbose:
        print(f"Processing {len(args.documents)} documents...")
        print(f"Persona: {args.persona}")
        print(f"Job: {args.job}")
        print(f"Output file: {args.output}")
    
    # Start timing
    start_time = time.time()
    
    try:
        # Initialize processor
        processor = DocumentProcessor()
        
        # Process documents
        result = processor.process_documents(args.documents, args.persona, args.job)
        
        # Calculate processing time
        processing_time = time.time() - start_time
        
        if args.verbose:
            print(f"Processing completed in {processing_time:.2f} seconds")
            print(f"Top section: {result['extracted_section']['section_title']}")
            print(f"Importance rank: {result['extracted_section']['importance_rank']:.3f}")
        
        # Save output
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        
        print(f"Results saved to {args.output}")
        
        # Check performance constraints
        if processing_time > 60:
            print(f"Warning: Processing time ({processing_time:.2f}s) exceeds 60-second constraint")
        
        return 0
        
    except Exception as e:
        print(f"Error during processing: {str(e)}")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 