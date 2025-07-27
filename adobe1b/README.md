# Persona-Driven Document Intelligence System

A sophisticated document analysis system that extracts and prioritizes relevant sections from PDF documents based on specific personas and job requirements. The system uses advanced NLP techniques to provide intelligent document insights while meeting strict performance constraints.

## Features

- **Intelligent Section Extraction**: Automatically identifies and extracts relevant sections from PDF documents
- **Persona-Based Analysis**: Tailors analysis to specific user roles and job requirements
- **Semantic Relevance Scoring**: Uses advanced NLP models for accurate content ranking
- **Multi-Document Processing**: Handles collections of 3-10 related documents
- **Structured JSON Output**: Provides detailed analysis in standardized format
- **Performance Optimized**: CPU-only operation with <60 second processing time
- **Offline Operation**: No internet access required during execution

## Technical Specifications

- **Model Size**: ≤1GB (all-MiniLM-L6-v2: ~90MB)
- **Processing Time**: ≤60 seconds for 3-5 documents
- **Platform**: CPU-only, no GPU required
- **Dependencies**: Offline operation, no external API calls
- **Input Format**: PDF documents
- **Output Format**: JSON with structured analysis

## Quick Start

### Using Docker (Recommended)

1. **Build the Docker image:**
   ```bash
   docker build -t persona-doc-intelligence .
   ```

2. **Run the system:**
   ```bash
   docker run -v $(pwd)/documents:/app/input_documents -v $(pwd)/output:/app/output \
     persona-doc-intelligence \
     python main.py \
     --documents /app/input_documents/doc1.pdf /app/input_documents/doc2.pdf \
     --persona "Investment Analyst" \
     --job "Analyze revenue trends and market positioning" \
     --output /app/output/result.json \
     --verbose
   ```

### Local Installation

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the system:**
   ```bash
   python main.py \
     --documents document1.pdf document2.pdf document3.pdf \
     --persona "PhD Researcher in Computational Biology" \
     --job "Prepare literature review on methodologies and datasets" \
     --output result.json \
     --verbose
   ```

## Usage Examples

### Example 1: Academic Research Analysis

```bash
python main.py \
  --documents research_paper1.pdf research_paper2.pdf research_paper3.pdf research_paper4.pdf \
  --persona "PhD Researcher in Computational Biology" \
  --job "Prepare a comprehensive literature review focusing on methodologies, datasets, and performance benchmarks" \
  --output academic_analysis.json
```

### Example 2: Business Financial Analysis

```bash
python main.py \
  --documents annual_report_2022.pdf annual_report_2023.pdf annual_report_2024.pdf \
  --persona "Investment Analyst" \
  --job "Analyze revenue trends, R&D investments, and market positioning strategies" \
  --output financial_analysis.json
```

### Example 3: Educational Content Analysis

```bash
python main.py \
  --documents chemistry_chapter1.pdf chemistry_chapter2.pdf chemistry_chapter3.pdf \
  --persona "Undergraduate Chemistry Student" \
  --job "Identify key concepts and mechanisms for exam preparation on reaction kinetics" \
  --output chemistry_analysis.json
```

## Output Format

The system generates a structured JSON output with the following format:

```json
{
  "metadata": {
    "input_documents": ["document1.pdf", "document2.pdf"],
    "persona": "Investment Analyst",
    "job_to_be_done": "Analyze revenue trends and market positioning",
    "processing_timestamp": "2024-01-15T10:30:00"
  },
  "extracted_section": {
    "document": "document1.pdf",
    "page_number": 5,
    "section_title": "Financial Performance",
    "importance_rank": 0.85
  },
  "sub_section_analysis": {
    "document": "document1.pdf",
    "subsection_id": 1,
    "refined_text": "Revenue increased by 15% year-over-year...",
    "page_number_constraints": 5
  }
}
```

## Command Line Arguments

| Argument | Required | Description | Example |
|----------|----------|-------------|---------|
| `--documents` | Yes | Paths to PDF documents | `doc1.pdf doc2.pdf` |
| `--persona` | Yes | Persona/role description | `"Investment Analyst"` |
| `--job` | Yes | Job to be done | `"Analyze revenue trends"` |
| `--output` | No | Output JSON file path | `result.json` |
| `--verbose` | No | Enable verbose output | Flag |

## Testing

Run the included test suite to verify system functionality:

```bash
python test_cases.py
```

This will execute three test cases:
1. **Academic Research**: 4 research papers on Graph Neural Networks
2. **Business Analysis**: 3 annual reports from tech companies
3. **Educational Content**: 5 chemistry textbook chapters

## Project Structure

```
adobe1b/
├── main.py                 # Main application entry point
├── document_processor.py   # Core document processing logic
├── test_cases.py          # Test cases and utilities
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── README.md             # This file
├── approach_explanation.md # Detailed methodology explanation
└── sample_output/        # Example output files
```

## Performance Considerations

- **Model Loading**: The sentence transformer model is loaded once and reused
- **Memory Usage**: Optimized for minimal memory footprint
- **Processing Speed**: Efficient text processing and scoring algorithms
- **Scalability**: Can handle larger document collections with linear scaling

## Troubleshooting

### Common Issues

1. **PDF Extraction Errors**: Ensure PDFs are not password-protected or corrupted
2. **Memory Issues**: For large documents, consider processing in smaller batches
3. **Slow Processing**: Check system resources and ensure adequate CPU availability

### Error Messages

- `Document not found`: Verify file paths are correct
- `Only PDF files are supported`: Ensure all input files are PDF format
- `Processing time exceeds 60-second constraint`: Consider reducing document count or complexity

## Contributing

This project is designed for the Adobe Persona-Driven Document Intelligence challenge. The system architecture is modular and can be extended for additional use cases.

## License

This project is created for educational and competition purposes.

## Support

For issues or questions, refer to the approach explanation document for technical details about the implementation methodology. 