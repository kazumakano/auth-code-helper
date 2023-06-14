Param (
    [parameter(mandatory=$True)] $Name,
    $HostName = '127.0.0.1',
    $Port = 5000,
    [switch] $Ssl
)

$proto = $Ssl ? 'https' : 'http'
curl "${proto}://${HostName}:$Port/qr/$Name"
