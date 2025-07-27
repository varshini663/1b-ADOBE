#!/usr/bin/env python3
"""
Test cases and utilities for the Persona-Driven Document Intelligence System.
"""

import json
import os
import tempfile
from pathlib import Path
from document_processor import DocumentProcessor

def create_sample_pdf_content(content: str, filename: str) -> str:
    """Create a temporary PDF file with sample content for testing."""
    # This is a simplified version - in a real scenario, you'd use a PDF library
    # For testing purposes, we'll create a text file that simulates PDF content
    temp_dir = tempfile.mkdtemp()
    file_path = os.path.join(temp_dir, filename)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return file_path

def create_test_case_1():
    """Create test case 1: Academic Research - Graph Neural Networks for Drug Discovery"""
    
    # Sample research paper content
    paper1_content = """
    GRAPH NEURAL NETWORKS FOR DRUG DISCOVERY
    
    Abstract
    This paper presents a comprehensive review of Graph Neural Networks (GNNs) 
    applied to drug discovery applications. We analyze various methodologies 
    and their performance on benchmark datasets.
    
    Introduction
    Drug discovery is a complex process that requires understanding molecular 
    structures and their interactions. Graph Neural Networks provide a powerful 
    framework for modeling molecular graphs.
    
    Methodology
    We implemented three different GNN architectures: Graph Convolutional Networks, 
    Graph Attention Networks, and GraphSAGE. Each model was trained on the 
    Tox21 dataset for toxicity prediction.
    
    Results
    Our experiments show that Graph Attention Networks achieve the best performance 
    with an AUC of 0.85 on the Tox21 dataset. The model successfully identifies 
    toxic compounds with high accuracy.
    
    Conclusion
    GNNs show promising results for drug discovery applications, particularly 
    in toxicity prediction and molecular property estimation.
    """
    
    paper2_content = """
    ADVANCED MOLECULAR REPRESENTATION LEARNING
    
    Abstract
    We propose a novel molecular representation learning approach using 
    hierarchical graph neural networks for improved drug discovery.
    
    Datasets and Benchmarks
    We evaluate our approach on multiple datasets including:
    - Tox21: Toxicity prediction
    - HIV: Anti-HIV activity prediction  
    - BACE: Beta-secretase 1 inhibition
    - BBBP: Blood-brain barrier penetration
    
    Performance Analysis
    Our hierarchical approach achieves state-of-the-art results across all 
    benchmark datasets, with significant improvements in prediction accuracy.
    """
    
    paper3_content = """
    COMPARATIVE STUDY OF DEEP LEARNING METHODS
    
    Introduction
    This study compares various deep learning approaches for molecular 
    property prediction in drug discovery.
    
    Methods
    We compare:
    1. Graph Neural Networks
    2. Convolutional Neural Networks on molecular fingerprints
    3. Recurrent Neural Networks on SMILES strings
    4. Transformer models on molecular graphs
    
    Experimental Setup
    All models were trained on the same datasets with identical preprocessing 
    and evaluation protocols to ensure fair comparison.
    
    Results and Discussion
    GNNs consistently outperform other approaches, particularly for tasks 
    requiring structural understanding of molecules.
    """
    
    paper4_content = """
    MOLECULAR GRAPH EMBEDDINGS FOR DRUG REPURPOSING
    
    Abstract
    We present a novel approach for drug repurposing using molecular graph 
    embeddings learned through graph neural networks.
    
    Background
    Drug repurposing aims to find new therapeutic uses for existing drugs, 
    potentially reducing development time and costs.
    
    Methodology
    Our approach learns continuous representations of molecular graphs that 
    capture both structural and functional properties of compounds.
    
    Validation
    We validate our approach on known drug-disease associations and demonstrate 
    its ability to predict novel therapeutic applications.
    """
    
    # Create temporary files
    files = []
    for i, content in enumerate([paper1_content, paper2_content, paper3_content, paper4_content], 1):
        filename = f"research_paper_{i}.pdf"
        file_path = create_sample_pdf_content(content, filename)
        files.append(file_path)
    
    return {
        "documents": files,
        "persona": "PhD Researcher in Computational Biology",
        "job": "Prepare a comprehensive literature review focusing on methodologies, datasets, and performance benchmarks",
        "expected_keywords": ["methodology", "datasets", "benchmarks", "performance", "Tox21", "HIV", "BACE"]
    }

def create_test_case_2():
    """Create test case 2: Business Analysis - Annual Reports"""
    
    # Sample annual report content
    report1_content = """
    APPLE INC. ANNUAL REPORT 2023
    
    Executive Summary
    Apple Inc. reported record revenue of $394.3 billion for fiscal year 2023, 
    representing a 2% increase over the previous year.
    
    Financial Performance
    Revenue Breakdown:
    - iPhone: $200.6 billion (51% of total revenue)
    - Mac: $29.4 billion (7% of total revenue)
    - iPad: $28.3 billion (7% of total revenue)
    - Wearables: $38.4 billion (10% of total revenue)
    - Services: $85.2 billion (22% of total revenue)
    
    Research and Development
    Apple invested $29.9 billion in R&D during 2023, representing 7.6% of 
    total revenue. Key focus areas include:
    - Artificial Intelligence and Machine Learning
    - Augmented Reality and Virtual Reality
    - Autonomous Systems
    - Health Technologies
    
    Market Positioning
    Apple maintains its premium positioning in the consumer electronics market, 
    with strong brand loyalty and ecosystem integration driving customer retention.
    """
    
    report2_content = """
    MICROSOFT CORPORATION ANNUAL REPORT 2023
    
    Financial Highlights
    Microsoft reported revenue of $211.9 billion for fiscal year 2023, 
    representing a 7% increase over the previous year.
    
    Revenue by Segment:
    - Productivity and Business Processes: $69.2 billion
    - Intelligent Cloud: $87.9 billion  
    - More Personal Computing: $54.7 billion
    
    Research and Development Investment
    Microsoft invested $27.2 billion in R&D, representing 12.8% of total revenue. 
    Key investment areas include:
    - Cloud Computing and Azure
    - Artificial Intelligence and Copilot
    - Gaming and Xbox
    - Enterprise Software Solutions
    
    Strategic Initiatives
    Microsoft continues to lead in cloud computing with Azure, while expanding 
    its AI capabilities through strategic partnerships and acquisitions.
    """
    
    report3_content = """
    GOOGLE (ALPHABET) ANNUAL REPORT 2023
    
    Financial Performance
    Alphabet reported revenue of $307.4 billion for fiscal year 2023, 
    representing a 9% increase over the previous year.
    
    Revenue Sources:
    - Google Advertising: $237.7 billion (77% of total revenue)
    - Google Other: $32.3 billion (11% of total revenue)
    - Google Cloud: $33.1 billion (11% of total revenue)
    - Other Bets: $1.5 billion (0.5% of total revenue)
    
    Research and Development
    Alphabet invested $39.5 billion in R&D, representing 12.8% of total revenue. 
    Focus areas include:
    - Artificial Intelligence and Large Language Models
    - Cloud Computing and Infrastructure
    - Autonomous Vehicles (Waymo)
    - Healthcare Technologies (Verily)
    
    Market Strategy
    Google continues to dominate digital advertising while expanding into 
    cloud computing and AI services to diversify revenue streams.
    """
    
    # Create temporary files
    files = []
    for i, content in enumerate([report1_content, report2_content, report3_content], 1):
        filename = f"annual_report_{i}.pdf"
        file_path = create_sample_pdf_content(content, filename)
        files.append(file_path)
    
    return {
        "documents": files,
        "persona": "Investment Analyst",
        "job": "Analyze revenue trends, R&D investments, and market positioning strategies",
        "expected_keywords": ["revenue", "R&D", "investment", "market", "positioning", "financial"]
    }

def create_test_case_3():
    """Create test case 3: Educational Content - Organic Chemistry"""
    
    # Sample chemistry textbook content
    chapter1_content = """
    CHAPTER 1: INTRODUCTION TO ORGANIC CHEMISTRY
    
    Organic Chemistry Fundamentals
    Organic chemistry is the study of carbon-containing compounds and their 
    reactions. Carbon's unique ability to form four covalent bonds makes it 
    the foundation of all living systems.
    
    Molecular Structure and Bonding
    Understanding molecular structure is crucial for predicting chemical 
    behavior. Key concepts include:
    - Lewis structures and electron dot diagrams
    - Valence bond theory
    - Molecular orbital theory
    - Hybridization of atomic orbitals
    
    Functional Groups
    Functional groups are specific arrangements of atoms that confer 
    characteristic chemical properties to molecules. Common functional groups include:
    - Hydroxyl groups (-OH)
    - Carbonyl groups (C=O)
    - Amino groups (-NH2)
    - Carboxyl groups (-COOH)
    """
    
    chapter2_content = """
    CHAPTER 2: REACTION MECHANISMS
    
    Understanding Reaction Mechanisms
    Reaction mechanisms describe the step-by-step process by which reactants 
    are converted to products. Understanding mechanisms is essential for:
    - Predicting reaction outcomes
    - Designing synthetic pathways
    - Optimizing reaction conditions
    
    Types of Reaction Mechanisms
    1. Substitution Reactions
       - SN1: Unimolecular nucleophilic substitution
       - SN2: Bimolecular nucleophilic substitution
    
    2. Elimination Reactions
       - E1: Unimolecular elimination
       - E2: Bimolecular elimination
    
    3. Addition Reactions
       - Electrophilic addition to alkenes
       - Nucleophilic addition to carbonyl compounds
    """
    
    chapter3_content = """
    CHAPTER 3: REACTION KINETICS
    
    Introduction to Kinetics
    Reaction kinetics is the study of reaction rates and the factors that 
    influence them. Understanding kinetics is crucial for:
    - Optimizing reaction conditions
    - Predicting reaction behavior
    - Designing efficient synthetic processes
    
    Rate Laws and Mechanisms
    The rate law expresses the relationship between reaction rate and 
    reactant concentrations:
    Rate = k[A]^m[B]^n
    
    Where:
    - k is the rate constant
    - m and n are reaction orders
    - [A] and [B] are reactant concentrations
    
    Factors Affecting Reaction Rates
    1. Temperature: Higher temperatures generally increase reaction rates
    2. Concentration: Higher reactant concentrations increase collision frequency
    3. Catalysts: Catalysts lower activation energy and increase rates
    4. Solvent effects: Solvent choice can significantly impact reaction rates
    """
    
    chapter4_content = """
    CHAPTER 4: STEREOCHEMISTRY
    
    Stereochemistry Fundamentals
    Stereochemistry deals with the three-dimensional arrangement of atoms 
    in molecules and its effect on chemical properties.
    
    Chirality and Enantiomers
    Chiral molecules have non-superimposable mirror images called enantiomers. 
    Enantiomers have identical physical properties but may differ in:
    - Biological activity
    - Optical rotation
    - Interaction with other chiral molecules
    
    Diastereomers and Meso Compounds
    Diastereomers are stereoisomers that are not mirror images of each other. 
    They have different physical and chemical properties.
    
    Stereochemistry in Reactions
    Understanding stereochemistry is crucial for:
    - Predicting reaction outcomes
    - Designing stereoselective syntheses
    - Understanding biological activity
    """
    
    chapter5_content = """
    CHAPTER 5: SPECTROSCOPY AND STRUCTURE DETERMINATION
    
    Introduction to Spectroscopy
    Spectroscopy techniques provide information about molecular structure 
    and composition through interaction with electromagnetic radiation.
    
    Infrared Spectroscopy (IR)
    IR spectroscopy provides information about functional groups present 
    in molecules by measuring vibrational transitions.
    
    Nuclear Magnetic Resonance (NMR)
    NMR spectroscopy is the most powerful tool for determining molecular 
    structure, providing information about:
    - Chemical environment of nuclei
    - Molecular connectivity
    - Stereochemistry
    
    Mass Spectrometry (MS)
    Mass spectrometry provides molecular weight and structural information 
    through ionization and fragmentation patterns.
    """
    
    # Create temporary files
    files = []
    for i, content in enumerate([chapter1_content, chapter2_content, chapter3_content, chapter4_content, chapter5_content], 1):
        filename = f"chemistry_chapter_{i}.pdf"
        file_path = create_sample_pdf_content(content, filename)
        files.append(file_path)
    
    return {
        "documents": files,
        "persona": "Undergraduate Chemistry Student",
        "job": "Identify key concepts and mechanisms for exam preparation on reaction kinetics",
        "expected_keywords": ["kinetics", "reaction", "mechanism", "rate", "activation", "catalyst"]
    }

def run_test_case(test_case: dict, test_name: str):
    """Run a test case and display results."""
    print(f"\n{'='*60}")
    print(f"Running Test Case: {test_name}")
    print(f"{'='*60}")
    
    try:
        # Initialize processor
        processor = DocumentProcessor()
        
        # Process documents
        result = processor.process_documents(
            test_case["documents"], 
            test_case["persona"], 
            test_case["job"]
        )
        
        # Display results
        print(f"Persona: {result['metadata']['persona']}")
        print(f"Job: {result['metadata']['job_to_be_done']}")
        print(f"Processing Time: {result['metadata']['processing_timestamp']}")
        
        print(f"\nExtracted Sections ({len(result['extracted_sections'])} total):")
        for i, section in enumerate(result['extracted_sections'][:3], 1):  # Show top 3
            print(f"  {i}. Document: {section['document']}")
            print(f"     Page: {section['page_number']}")
            print(f"     Title: {section['section_title']}")
            print(f"     Importance Rank: {section['importance_rank']:.3f}")
        
        print(f"\nSubsection Analyses ({len(result['sub_section_analyses'])} total):")
        for i, subsection in enumerate(result['sub_section_analyses'][:3], 1):  # Show top 3
            print(f"  {i}. Document: {subsection['document']}")
            print(f"     ID: {subsection['subsection_id']}")
            print(f"     Text: {subsection['refined_text'][:150]}...")
            print(f"     Importance Rank: {subsection['importance_rank']:.3f}")
        
        # Save results
        output_file = f"test_output_{test_name.lower().replace(' ', '_')}.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        
        print(f"\nResults saved to: {output_file}")
        
        return True
        
    except Exception as e:
        print(f"Error running test case: {str(e)}")
        return False

def main():
    """Run all test cases."""
    print("Persona-Driven Document Intelligence System - Test Suite")
    print("=" * 60)
    
    # Create and run test cases
    test_cases = [
        ("Academic Research", create_test_case_1()),
        ("Business Analysis", create_test_case_2()),
        ("Educational Content", create_test_case_3())
    ]
    
    results = []
    for test_name, test_case in test_cases:
        success = run_test_case(test_case, test_name)
        results.append((test_name, success))
    
    # Summary
    print(f"\n{'='*60}")
    print("TEST SUMMARY")
    print(f"{'='*60}")
    
    for test_name, success in results:
        status = "PASSED" if success else "FAILED"
        print(f"{test_name}: {status}")
    
    print(f"\nAll test outputs saved as JSON files.")

if __name__ == "__main__":
    main() 