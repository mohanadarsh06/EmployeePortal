#!/usr/bin/env python
"""
Script to initialize the application database from an Excel file.
Usage: python init_from_excel.py <path_to_excel_file>
"""
import os
import sys
from flask import Flask
from app import create_app
from app.models import db
from app.utils.excel_import import import_employees_from_excel
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def init_from_excel(excel_path):
    """Initialize the application database from an Excel file."""
    if not os.path.exists(excel_path):
        logger.error(f"File not found: {excel_path}")
        return False
    
    # Create the application
    logger.info("Creating application...")
    app = create_app()
    
    with app.app_context():
        # Check if database already has data
        from app.models import Employee
        if Employee.query.count() > 0:
            logger.warning("Database already contains employee data. Import aborted.")
            return False
        
        # Import employees from Excel
        logger.info(f"Importing employees from {excel_path}...")
        result = import_employees_from_excel(excel_path)
        
        if result["success"]:
            logger.info(f"Successfully imported {result['created']} employees.")
            if result["errors"]:
                logger.warning(f"Encountered {len(result['errors'])} errors during import:")
                for error in result["errors"]:
                    logger.warning(f"  Row {error.get('row', 'unknown')}: {error.get('error', 'Unknown error')}")
            return True
        else:
            logger.error(f"Import failed: {result.get('error', 'Unknown error')}")
            return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python init_from_excel.py <path_to_excel_file>")
        sys.exit(1)
    
    excel_path = sys.argv[1]
    success = init_from_excel(excel_path)
    
    if success:
        print("\nImport completed successfully!")
        print("You can now run the application with 'python run.py'")
    else:
        print("\nImport failed. Please check the logs for details.")
        sys.exit(1)