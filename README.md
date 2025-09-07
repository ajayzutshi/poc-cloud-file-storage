# Simple Cloud File Storage System

### Developed by: Ajay Zutshi
### Student of: Indo Global College of Engineering

## Project Overview:
This project is a simple file storage system where users can upload PDF and image files via a web interface.  
Files are stored in AWS S3, and daily backups are automated using AWS Lambda.



## Prerequisites  
- Python 3.8+  
- AWS Free Tier Account  
- Two S3 Buckets (one for primary storage, one for backup)  



## Setup Instructions  

1. Install dependencies:  
   ```bash
   pip install flask boto3
