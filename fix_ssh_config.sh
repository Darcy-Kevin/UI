#!/bin/zsh

# This script will help you fix your SSH configuration for GitHub
# It will backup your current SSH config and update it to use the correct key

echo "Creating backup of your current SSH config..."
mkdir -p ~/.ssh/backup
cp ~/.ssh/config ~/.ssh/backup/config.bak.$(date +%Y%m%d_%H%M%S)

echo "Updating SSH config to use the correct key..."
cat > ~/.ssh/config.new << EOF
# --- Updated SSH Config for GitHub ---
Host github.com
  HostName github.com
  User git
  PreferredAuthentications publickey
  IdentityFile ~/.ssh/id_ed25519
  UseKeychain yes
  AddKeysToAgent yes
  # Optional: Add timeout settings to avoid connection issues
  ConnectTimeout 30
  ServerAliveInterval 60
  ServerAliveCountMax 3
EOF

echo ""
echo "Preview of the new SSH config:"
echo "------------------------------------"
cat ~/.ssh/config.new
echo "------------------------------------"

echo ""
echo "To apply this new configuration, run:"
echo "cp ~/.ssh/config.new ~/.ssh/config"
echo ""
echo "After updating, test your connection with:"
echo "ssh -T git@github.com"
echo ""
echo "This will fix the 'no such identity: /Users/duole-b-01/.ssh/Darcy-Kevin-GitHub' error."