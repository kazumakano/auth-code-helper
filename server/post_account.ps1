Param (
    [parameter(mandatory=$True)] $Name,
    [parameter(mandatory=$True)] $Seed,
    $HostName = '127.0.0.1',
    $Port = 5000
)

curl --data "{\""name\"": \""$Name\"", \""seed\"": \""$Seed\""}" --header 'Content-Type: application/json' --request 'POST' "http://${HostName}:$Port/account"
