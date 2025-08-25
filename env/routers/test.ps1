# Load server list
$Servers = Get-Content servers.txt

# Source and destination
$Source = "\\networkshare\patches"
$Destination = "C:\Temp\Patches"

# Get credentials once
$Cred = Get-Credential

# Create log file
$LogFile = "patch_copy_log.txt"
"" | Out-File $LogFile

# Run in parallel (PowerShell 7+ required)
$Servers | ForEach-Object -Parallel {
    param($Source, $Destination, $Cred, $LogFile)

    try {
        $Session = New-PSSession -ComputerName $_ -Credential $Cred -ErrorAction Stop
        Copy-Item -Path "$Source\*" -Destination $Destination -ToSession $Session -Recurse -Force -ErrorAction Stop
        Remove-PSSession $Session
        Add-Content -Path $LogFile -Value "$_ : SUCCESS"
    }
    catch {
        Add-Content -Path $LogFile -Value "$_ : FAILED - $($_.Exception.Message)"
    }

} -ArgumentList $Source, $Destination, $Cred, $LogFile -ThrottleLimit 20