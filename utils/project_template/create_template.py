#!/usr/bin/env python3
"""
RHS Altium Project Template Creator

This script creates a project template from the files in the 'files/' directory.

Usage:
    python create_template.py [options]

Examples:
    python create_template.py
    python create_template.py --name "MyProject"
    python create_template.py --name "TestBoard" --format tar.gz
    python create_template.py --output-dir /path/to/output
"""

import argparse
import os
import shutil
import zipfile
import tarfile
from datetime import datetime
from pathlib import Path
import sys


class TemplateCreator:
    def __init__(self, project_name=None, output_dir=None):
        self.project_name = project_name or "rhs-altium-template"
        self.timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
        self.template_dir = f"{self.project_name}-{self.timestamp}"

        # Set paths
        self.script_dir = Path(__file__).parent
        self.output_dir = Path(output_dir) if output_dir else self.script_dir
        self.template_path = self.output_dir / self.template_dir
        self.files_dir = self.script_dir / "../../template/"

    def validate_source_files(self):
        """Validate that required source files exist"""
        if not self.files_dir.exists():
            raise FileNotFoundError(f"Files directory not found: {self.files_dir}")

    def create_template_directory(self):
        """Create the template directory structure"""
        print(f"🔧 Creating project template...")
        print(f"📁 Directory: {self.template_dir}")

        print("")

        # Create template directory
        self.template_path.mkdir(parents=True, exist_ok=True)

    def copy_files(self):
        """Copy core template files"""
        print("📋 Copying template files...")

        template_src = self.files_dir
        if template_src.exists():
            for item in template_src.glob('*'):
                if item.is_file():
                    dst = self.template_path / item.name
                    shutil.copy2(item, dst)
                    print(f"   ✓ {item.name}")
                elif item.is_dir():
                    dst = self.template_path / item.name
                    shutil.copytree(item, dst)
                    print(f"   ✓ {item.name}/ (directory)")
        else:
            print("   ⚠️ Template directory not found")

    def create_template_info(self):
        """Create template information file"""
        info_content = f"""RHS Altium Project Template
===========================

Generated: {self.timestamp}
Template Name: {self.template_dir}
Script: create_template.py
Project Name: {self.project_name}
Full manual: https://roboticshardwaresolutions.github.io/altguide/

"""

        info_path = self.template_path / "TEMPLATE_INFO.txt"
        info_path.write_text(info_content, encoding='utf-8')
        print("   ✓ Template info")

    def create_archive(self):
        """Create archive of the template"""
        print("📦 Creating archive...")

        archive_format = "zip"  # или добавьте параметр в __init__
        archive_name = f"{self.template_dir}.{archive_format}"
        archive_path = self.output_dir / archive_name
        self._create_zip_archive(archive_path)
        return archive_path

    def _create_zip_archive(self, archive_path):
        """Create ZIP archive"""
        with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as zf:
            for file_path in self.template_path.rglob('*'):
                if file_path.is_file():
                    arcname = file_path.relative_to(self.output_dir)
                    zf.write(file_path, arcname)
        print(f"   ✓ ZIP archive: {archive_path.name}")

    def cleanup(self, keep_directory=False):
        """Clean up temporary files"""
        if not keep_directory and self.template_path.exists():
            shutil.rmtree(self.template_path)
            print(f"🧹 Cleaned up temporary directory: {self.template_dir}")

    def create_template(self, keep_directory=False):
        """Main method to create the template"""
        try:
            self.validate_source_files()
            self.create_template_directory()
            self.copy_files()
            self.create_template_info()
            archive_path = self.create_archive()

            if not keep_directory:
                self.cleanup()

            print("")
            print("✅ Template created successfully!")
            if keep_directory:
                print(f"📁 Directory: {self.template_path}")
            print(f"📦 Archive: {archive_path}")
            print("")
            print("🚀 To use:")
            print("   1. Extract archive to new project directory")
            print("   2. Open proj.pcbdoc in Altium Designer")
            print("   3. Enjoy")
            print("")

            return archive_path

        except Exception as e:
            print(f"❌ Error creating template: {e}")
            self.cleanup()
            sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Create RHS Altium project template",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s
  %(prog)s --name "MyProject"
  %(prog)s --output-dir /path/to/output --keep-dir
        """
    )

    parser.add_argument(
        "--name", "-n",
        default="rhs-altium-template",
        help="Project name (default: rhs-altium-template)"
    )

    parser.add_argument(
        "--output-dir", "-o",
        help="Output directory (default: current directory)"
    )
    parser.add_argument(
        "--keep-dir",
        action="store_true",
        help="Keep template directory after creating archive"
    )
    parser.add_argument(
        "--version", "-v",
        action="version",
        version="RHS Template Creator 0.1.1"
    )
    args = parser.parse_args()
    creator = TemplateCreator(
        project_name=args.name,
        output_dir=args.output_dir
    )

    creator.create_template(keep_directory=args.keep_dir)


if __name__ == "__main__":
    main()
