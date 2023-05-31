$vpnServerIP = "10.145.20.45"  # Replace with your VPN server IP

$vpnServerIPHex = [System.BitConverter]::ToString([System.Net.IPAddress]::Parse($vpnServerIP).GetAddressBytes()).Replace("-", "")
Write-Host "VPN Server IP Hex: $vpnServerIPHex"
