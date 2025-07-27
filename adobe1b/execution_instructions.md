# Execution Instructions

This document provides detailed instructions for running the Persona-Driven Document Intelligence System in various environments.

## Prerequisites

### System Requirements
- **Operating System**: Windows, macOS, or Linux
- **Python**: Version 3.8 or higher
- **Memory**: Minimum 2GB RAM (4GB recommended)
- **Storage**: At least 500MB free space for models and dependencies
- **CPU**: Multi-core processor recommended for optimal performance

### Software Dependencies
- Python 3.8+
- pip (Python package installer)
- Docker (optional, for containerized execution)

## Installation Methods

### Method 1: Local Python Installation (Recommended for Development)

1. **Clone or download the project:**
   ```bash
   git clone <repository-url>
   cd adobe1b
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify installation:**
   ```bash
   python -c "import PyPDF2, sentence_transformers, numpy, sklearn, pandas; print('All dependencies installed successfully!')"
   ```

### Method 2: Docker Installation (Recommended for Production)

1. **Build the Docker image:**
   ```bash
   docker build -t persona-doc-intelligence .
   ```

2. **Verify the image was created:**
   ```bash
   docker images | grep persona-doc-intelligence
   ```

## Running the System

### Basic Usage

The system can be run using the `main.py` script with the following required parameters:

```bash
python main.py \
  --documents <path-to-pdf1> <path-to-pdf2> ... \
  --persona "<persona-description>" \
  --job "<job-description>" \
  [--output <output-file>] \
  [--verbose]
```

### Example Commands

#### Example 1: Academic Research Analysis
```bash
python main.py \
  --documents research_paper1.pdf research_paper2.pdf research_paper3.pdf \
  --persona "PhD Researcher in Computational Biology" \
  --job "Prepare a comprehensive literature review focusing on methodologies, datasets, and performance benchmarks" \
  --output academic_analysis.json \
  --verbose
```

#### Example 2: Business Financial Analysis
```bash
python main.py \
  --documents annual_report_2022.pdf annual_report_2023.pdf annual_report_2024.pdf \
  --persona "Investment Analyst" \
  --job "Analyze revenue trends, R&D investments, and market positioning strategies" \
  --output financial_analysis.json \
  --verbose
```

#### Example 3: Educational Content Analysis
```bash
python main.py \
  --documents chemistry_chapter1.pdf chemistry_chapter2.pdf chemistry_chapter3.pdf \
  --persona "Undergraduate Chemistry Student" \
  --job "Identify key concepts and mechanisms for exam preparation on reaction kinetics" \
  --output chemistry_analysis.json \
  --verbose
```

### Docker Usage

#### Running with Docker
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

#### Windows Docker Command
```cmd
docker run -v %cd%/documents:/app/input_documents -v %cd%/output:/app/output ^
  persona-doc-intelligence ^
  python main.py ^
  --documents /app/input_documents/doc1.pdf /app/input_documents/doc2.pdf ^
  --persona "Investment Analyst" ^
  --job "Analyze revenue trends and market positioning" ^
  --output /app/output/result.json ^
  --verbose
```

## Testing the System

### Running Test Cases

1. **Execute the test suite:**
   ```bash
   python test_cases.py
   ```

2. **Or use the provided script:**
   ```bash
   # On Linux/macOS:
   ./run_tests.sh
   
   # On Windows:
   bash run_tests.sh
   ```

### Expected Test Output

The test suite will run three test cases and generate the following files:
- `test_output_academic_research.json`
- `test_output_business_analysis.json`
- `test_output_educational_content.json`

### Sample Output Validation

After running tests, verify the output format matches the expected structure:

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

## Performance Monitoring

### Processing Time
- The system is designed to process 3-5 documents within 60 seconds
- Monitor processing time in verbose mode
- Warning will be displayed if processing exceeds 60 seconds

### Memory Usage
- Model loading requires ~200MB RAM
- Processing memory scales with document size
- Monitor system resources during execution

### CPU Utilization
- The system is CPU-optimized
- Multi-core processors will see improved performance
- No GPU acceleration required

## Troubleshooting

### Common Issues and Solutions

#### 1. PDF Extraction Errors
**Problem**: "Error processing document.pdf"
**Solution**: 
- Ensure PDFs are not password-protected
- Verify PDFs are not corrupted
- Check file permissions

#### 2. Model Download Issues
**Problem**: "Error downloading model"
**Solution**:
- Check internet connection during first run
- Verify sufficient disk space
- Clear pip cache: `pip cache purge`

#### 3. Memory Issues
**Problem**: "Out of memory" errors
**Solution**:
- Close other applications
- Process documents in smaller batches
- Increase system RAM if possible

#### 4. Slow Processing
**Problem**: Processing time > 60 seconds
**Solution**:
- Check CPU utilization
- Reduce document count
- Ensure adequate system resources

### Error Messages and Meanings

| Error Message | Meaning | Solution |
|---------------|---------|----------|
| "Document not found" | File path is incorrect | Verify file paths |
| "Only PDF files are supported" | Non-PDF file provided | Convert to PDF or use PDF files |
| "Persona is required" | Missing persona parameter | Provide --persona argument |
| "Job to be done is required" | Missing job parameter | Provide --job argument |

## Advanced Configuration

### Environment Variables
```bash
export PYTHONPATH=/path/to/project
export PYTHONUNBUFFERED=1
```

### Custom Model Configuration
To use a different sentence transformer model, modify `document_processor.py`:
```python
self.model = SentenceTransformer('your-preferred-model')
```

### Output Customization
The output format can be customized by modifying the `process_documents` method in `document_processor.py`.

## Support and Documentation

- **README.md**: General project overview and quick start
- **approach_explanation.md**: Detailed technical methodology
- **test_cases.py**: Comprehensive test suite
- **sample_output/**: Example output files

For additional support, refer to the project documentation or check the error logs for specific issues. 