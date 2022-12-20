Param (
    [parameter(mandatory=$True)] $Name,
    $HostName = '127.0.0.1',
    $Port = 5000
)

curl "http://${HostName}:$Port/qr/$Name"
