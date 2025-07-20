#!/usr/bin/env python3
"""
Notebook Cleaner Script for OTT Analytics
Removes outputs and execution counts from Jupyter notebooks to keep Git diffs clean
"""

import json
import sys
from pathlib import Path

def clean_notebook(notebook_path):
    """
    Clean a Jupyter notebook by removing outputs and execution counts
    """
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        # Track changes
        cells_cleaned = 0
        
        # Clean each cell
        for cell in notebook.get('cells', []):
            if cell.get('cell_type') == 'code':
                # Remove outputs
                if 'outputs' in cell and cell['outputs']:
                    cell['outputs'] = []
                    cells_cleaned += 1
                
                # Remove execution count
                if 'execution_count' in cell and cell['execution_count'] is not None:
                    cell['execution_count'] = None
        
        # Remove kernel info and metadata that can cause diffs
        if 'metadata' in notebook:
            # Keep only essential metadata
            essential_metadata = {
                'kernelspec': notebook['metadata'].get('kernelspec', {}),
                'language_info': {
                    'name': notebook['metadata'].get('language_info', {}).get('name', 'python')
                }
            }
            notebook['metadata'] = essential_metadata
        
        # Save cleaned notebook
        with open(notebook_path, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Cleaned {notebook_path.name}: {cells_cleaned} cells cleaned")
        return True
        
    except Exception as e:
        print(f"❌ Error cleaning {notebook_path.name}: {e}")
        return False

def main():
    """Main function to clean notebooks"""
    project_dir = Path(__file__).parent
    
    # Find all notebook files
    notebook_files = list(project_dir.glob("*.ipynb"))
    
    if not notebook_files:
        print("No notebook files found in the current directory")
        return
    
    print(f"Found {len(notebook_files)} notebook file(s) to clean:")
    
    cleaned_count = 0
    for notebook_file in notebook_files:
        print(f"\n🧹 Cleaning {notebook_file.name}...")
        if clean_notebook(notebook_file):
            cleaned_count += 1
    
    print(f"\n✨ Cleaning complete! {cleaned_count}/{len(notebook_files)} notebooks cleaned successfully")
    print("\n💡 Tip: Run this script before committing to keep your Git history clean!")

if __name__ == "__main__":
    main()
