#!/usr/bin/env bash
set -euo pipefail

# Convert all .kismet files in /home/$USER/kismet_logs/ to .pcapng in ./pcap/
for kismet_file in /home/$USER/kismet_logs/*.kismet; do
  # Get base filename without extension
  base_name=$(basename "$kismet_file" .kismet)
  out_file="/home/$USER/pcap/${base_name}.pcapng"
  echo "Converting $kismet_file to $out_file"
  kismetdb_to_pcap --in "$kismet_file" --out "$out_file"
done

echo "All conversions complete."
