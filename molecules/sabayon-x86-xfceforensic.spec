# Use abs path, otherwise daily builds automagic won't work
%env %import ${SABAYON_MOLECULE_HOME:-/sabayon}/molecules/forensicxfce.common

prechroot: linux32

# Release Version
release_version: 9

# Release Version string description
release_desc: x86 ForensicsXfce

# Path to source ISO file (MANDATORY)
%env source_iso: ${SABAYON_MOLECULE_HOME:-/sabayon}/iso/Sabayon_Linux_DAILY_x86_Xfce.iso

destination_iso_image_name: Sabayon_Linux_DAILY_x86_ForensicsXfce.iso
