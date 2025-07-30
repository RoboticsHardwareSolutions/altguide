#!/usr/bin/env python3
"""
RHS Altium Project Template Creator

This script creates a project template from the files in the 'files/' directory
and optionally includes the altlib component libraries.

Usage:
    python create_template.py [options]

Examples:
    python create_template.py
    python create_template.py --name "MyProject" --no-altlib
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
    def __init__(self, project_name=None, include_altlib=False, output_dir=None, 
                 archive_format="zip", include_workflows=True, include_docs=True):
        self.project_name = project_name or "rhs-altium-template"
        self.include_altlib = include_altlib
        self.include_workflows = include_workflows
        self.include_docs = include_docs
        self.archive_format = archive_format
        self.timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
        self.template_dir = f"{self.project_name}-{self.timestamp}"
        
        # Set paths
        self.script_dir = Path(__file__).parent
        self.output_dir = Path(output_dir) if output_dir else self.script_dir
        self.template_path = self.output_dir / self.template_dir
        
        # Source directories
        self.files_dir = self.script_dir / "files"
        self.altlib_dir = self.script_dir / "altlib"
        self.guide_file = self.script_dir / "altguide.md"
        
    def validate_source_files(self):
        """Validate that required source files exist"""
        if not self.files_dir.exists():
            raise FileNotFoundError(f"Files directory not found: {self.files_dir}")
        
        required_files = ["PCB.PcbDoc", "Job.OutJob", "board_options.txt", "ext_bom.csv"]
        missing_files = []
        
        for file in required_files:
            if not (self.files_dir / file).exists():
                missing_files.append(file)
        
        if missing_files:
            raise FileNotFoundError(f"Required files missing: {', '.join(missing_files)}")
        
        if self.include_altlib and not self.altlib_dir.exists():
            print(f"⚠️ Warning: altlib directory not found: {self.altlib_dir}")
            self.include_altlib = False
        
        if self.include_docs and not self.guide_file.exists():
            print(f"⚠️ Warning: guide file not found: {self.guide_file}")
            self.include_docs = False
    
    def create_template_directory(self):
        """Create the template directory structure"""
        print(f"🔧 Creating project template...")
        print(f"📁 Directory: {self.template_dir}")
        print(f"📚 Include altlib: {self.include_altlib}")
        print(f"⚙️ Include workflows: {self.include_workflows}")
        print(f"📖 Include docs: {self.include_docs}")
        print("")
        
        # Create template directory
        self.template_path.mkdir(parents=True, exist_ok=True)
    
    def copy_core_files(self):
        """Copy core PCB files"""
        print("📋 Copying core files...")
        
        core_files = ["PCB.PcbDoc", "Job.OutJob", "board_options.txt", "ext_bom.csv"]
        
        for file in core_files:
            src = self.files_dir / file
            dst = self.template_path / file
            if src.exists():
                shutil.copy2(src, dst)
                print(f"   ✓ {file}")
        
        # Copy .gitignore if exists
        gitignore_src = self.files_dir / ".gitignore.gitignore"
        if gitignore_src.exists():
            gitignore_dst = self.template_path / ".gitignore"
            shutil.copy2(gitignore_src, gitignore_dst)
            print("   ✓ .gitignore")
    
    def copy_workflows(self):
        """Copy GitHub workflows"""
        if not self.include_workflows:
            return
            
        print("⚙️ Copying GitHub workflows...")
        
        workflows_src = self.files_dir / ".github"
        if workflows_src.exists():
            workflows_dst = self.template_path / ".github"
            shutil.copytree(workflows_src, workflows_dst, dirs_exist_ok=True)
            print("   ✓ GitHub workflows")
        else:
            print("   ⚠️ No workflows found")
    
    def copy_altlib(self):
        """Copy altlib libraries"""
        if not self.include_altlib:
            return
            
        print("📚 Copying altlib libraries...")
        
        if self.altlib_dir.exists():
            altlib_dst = self.template_path / "altlib"
            shutil.copytree(self.altlib_dir, altlib_dst, dirs_exist_ok=True)
            print("   ✓ Component libraries")
        else:
            print("   ⚠️ Altlib directory not found")
    
    def copy_documentation(self):
        """Copy documentation files"""
        if not self.include_docs:
            return
            
        print("📖 Copying documentation...")
        
        if self.guide_file.exists():
            guide_dst = self.template_path / "PROJECT_SETUP_GUIDE.md"
            shutil.copy2(self.guide_file, guide_dst)
            print("   ✓ Setup guide")
        else:
            print("   ⚠️ Guide file not found")
    
    def create_readme(self):
        """Create README.md for the template"""
        print("📝 Creating README.md...")
        
        readme_content = f"""# {self.project_name}

## Documentation:
[all documentation files](doc/pcb/)<br>
[schematic](<doc/pcb/Schematic Prints.PDF>)<br>
[assembly drawings](<doc/pcb/Assembly Drawings.PDF>)<br>
[board options](doc/pcb/board_options.txt)

## Pinout and PCB image
![pinout](doc/pinout/pinout.png)<br>
![top](doc/photo/top.png)<br>
![bottom](doc/photo/bot.png)

## Development

This project was created using the RHS Altium template.

### Project Structure
- `PCB.PcbDoc` - Main PCB design file
- `Job.OutJob` - Output job configuration
- `board_options.txt` - Manufacturing specifications
- `ext_bom.csv` - External BOM template"""

        if self.include_altlib:
            readme_content += "\n- `altlib/` - RHS component libraries"
        
        if self.include_workflows:
            readme_content += "\n- `.github/workflows/` - CI/CD workflows"
        
        readme_content += """

### Getting Started
1. Open PCB.PcbDoc in Altium Designer
2. Configure your schematic and PCB layout
3. Update board_options.txt with your specifications
4. Use Job.OutJob to generate manufacturing files

### Support
For template issues: https://github.com/RoboticsHardwareSolutions/altguide
"""
        
        readme_path = self.template_path / "README.md"
        readme_path.write_text(readme_content, encoding='utf-8')
        print("   ✓ README.md")
    
    def create_template_info(self):
        """Create template information file"""
        info_content = f"""RHS Altium Project Template
===========================

Generated: {self.timestamp}
Template Name: {self.template_dir}
Script: create_template.py

Included Components:
- Core PCB files: ✓
- GitHub workflows: {'✓' if self.include_workflows else '✗'}
- RHS libraries: {'✓' if self.include_altlib else '✗'}
- Documentation: {'✓' if self.include_docs else '✗'}

Project Name: {self.project_name}
Archive Format: {self.archive_format}
"""
        
        info_path = self.template_path / "TEMPLATE_INFO.txt"
        info_path.write_text(info_content, encoding='utf-8')
        print("   ✓ Template info")
    
    def create_archive(self):
        """Create archive of the template"""
        print("📦 Creating archive...")
        
        archive_name = f"{self.template_dir}.{self.archive_format}"
        archive_path = self.output_dir / archive_name
        
        if self.archive_format == "zip":
            self._create_zip_archive(archive_path)
        elif self.archive_format in ["tar.gz", "tgz"]:
            self._create_tar_archive(archive_path, "gz")
        elif self.archive_format == "tar":
            self._create_tar_archive(archive_path)
        else:
            raise ValueError(f"Unsupported archive format: {self.archive_format}")
        
        return archive_path
    
    def _create_zip_archive(self, archive_path):
        """Create ZIP archive"""
        with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as zf:
            for file_path in self.template_path.rglob('*'):
                if file_path.is_file():
                    arcname = file_path.relative_to(self.output_dir)
                    zf.write(file_path, arcname)
        print(f"   ✓ ZIP archive: {archive_path.name}")
    
    def _create_tar_archive(self, archive_path, compression=None):
        """Create TAR archive"""
        mode = "w"
        if compression:
            mode += f":{compression}"
        
        with tarfile.open(archive_path, mode) as tf:
            tf.add(self.template_path, arcname=self.template_dir)
        
        archive_type = f"TAR.{compression.upper()}" if compression else "TAR"
        print(f"   ✓ {archive_type} archive: {archive_path.name}")
    
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
            self.copy_core_files()
            self.copy_workflows()
            self.copy_altlib()
            self.copy_documentation()
            self.create_readme()
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
            print("   2. Open PCB.PcbDoc in Altium Designer")
            print("   3. Configure project for your needs")
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
  %(prog)s --name "MyProject" --no-altlib
  %(prog)s --name "TestBoard" --format tar.gz
  %(prog)s --output-dir /path/to/output --keep-dir
        """
    )
    
    parser.add_argument(
        "--name", "-n",
        default="rhs-altium-template",
        help="Project name (default: rhs-altium-template)"
    )
    
    parser.add_argument(
        "--no-altlib",
        action="store_true",
        help="Don't include altlib component libraries"
    )
    
    parser.add_argument(
        "--no-workflows",
        action="store_true",
        help="Don't include GitHub workflows"
    )
    
    parser.add_argument(
        "--no-docs",
        action="store_true",
        help="Don't include documentation"
    )
    
    parser.add_argument(
        "--format", "-f",
        choices=["zip", "tar", "tar.gz", "tgz"],
        default="zip",
        help="Archive format (default: zip)"
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
        version="RHS Template Creator 1.0.0"
    )
    
    args = parser.parse_args()
    
    creator = TemplateCreator(
        project_name=args.name,
        include_altlib=not args.no_altlib,
        include_workflows=not args.no_workflows,
        include_docs=not args.no_docs,
        archive_format=args.format,
        output_dir=args.output_dir
    )
    
    creator.create_template(keep_directory=args.keep_dir)


if __name__ == "__main__":
    main()
