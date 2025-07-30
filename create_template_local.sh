#!/bin/bash

# Script for local project template creation
# Usage: ./create_template_local.sh [project_name] [include_altlib]

PROJECT_NAME=${1:-"rhs-altium-template"}
INCLUDE_ALTLIB=${2:-"true"}
TIMESTAMP=$(date +'%Y%m%d-%H%M%S')
TEMPLATE_DIR="${PROJECT_NAME}-${TIMESTAMP}"

echo "🔧 Creating project template..."
echo "📁 Directory: ${TEMPLATE_DIR}"
echo "📚 Include altlib: ${INCLUDE_ALTLIB}"
echo ""

# Create template directory
mkdir -p "${TEMPLATE_DIR}"

# Copy core files
echo "📋 Copying core files..."
cp files/PCB.PcbDoc "${TEMPLATE_DIR}/"
cp files/Job.OutJob "${TEMPLATE_DIR}/"
cp files/board_options.txt "${TEMPLATE_DIR}/"
cp files/ext_bom.csv "${TEMPLATE_DIR}/"

# Copy .gitignore if exists
if [ -f files/.gitignore.gitignore ]; then
    cp files/.gitignore.gitignore "${TEMPLATE_DIR}/.gitignore"
fi

# Copy GitHub workflows
echo "⚙️ Copying GitHub workflows..."
mkdir -p "${TEMPLATE_DIR}/.github"
cp -r files/.github/* "${TEMPLATE_DIR}/.github/"

# Copy altlib if needed
if [ "${INCLUDE_ALTLIB}" = "true" ]; then
    echo "📚 Copying altlib libraries..."
    cp -r altlib "${TEMPLATE_DIR}/"
fi

# Copy documentation
echo "📖 Copying documentation..."
cp altguide.md "${TEMPLATE_DIR}/PROJECT_SETUP_GUIDE.md"

# Create README.md
echo "📝 Creating README.md..."
cat > "${TEMPLATE_DIR}/README.md" << EOF
# ${PROJECT_NAME}

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
- \`PCB.PcbDoc\` - Main PCB design file
- \`Job.OutJob\` - Output job configuration
- \`board_options.txt\` - Manufacturing specifications
- \`ext_bom.csv\` - External BOM template
EOF

if [ "${INCLUDE_ALTLIB}" = "true" ]; then
    echo "- \`altlib/\` - RHS component libraries" >> "${TEMPLATE_DIR}/README.md"
fi

cat >> "${TEMPLATE_DIR}/README.md" << 'EOF'
- `.github/workflows/` - CI/CD workflows

### Getting Started
1. Open PCB.PcbDoc in Altium Designer
2. Configure your schematic and PCB layout
3. Update board_options.txt with your specifications
4. Use Job.OutJob to generate manufacturing files

### Support
For template issues: https://github.com/RoboticsHardwareSolutions/altguide
EOF

# Create information file
cat > "${TEMPLATE_DIR}/TEMPLATE_INFO.txt" << EOF
RHS Altium Project Template
===========================

Generated: ${TIMESTAMP}
Template Name: ${TEMPLATE_DIR}
Script: create_template_local.sh

Included Components:
- Core PCB files: ✓
- GitHub workflows: ✓
- RHS libraries: $([ "${INCLUDE_ALTLIB}" = "true" ] && echo "✓" || echo "✗")
- Documentation: ✓

Project Name: ${PROJECT_NAME}
EOF

# Create archive
echo "📦 Creating archive..."
zip -r "${TEMPLATE_DIR}.zip" "${TEMPLATE_DIR}/" > /dev/null

echo ""
echo "✅ Template created successfully!"
echo "📁 Directory: ${TEMPLATE_DIR}/"
echo "📦 Archive: ${TEMPLATE_DIR}.zip"
echo ""
echo "🚀 To use:"
echo "   1. Extract archive to new project directory"
echo "   2. Open PCB.PcbDoc in Altium Designer"
echo "   3. Configure project for your needs"
echo ""
