const copyCode = async () => {
  // edit here
  const NAME = "foo"
  const SERVER_HOST = "https://127.0.0.1"
  const SERVER_PORT = 5000

  const code = await (await fetch(`${SERVER_HOST}:${SERVER_PORT}/code/${NAME}`)).text()
  console.log(`authentification code is ${code}`)

  await window.navigator.clipboard.writeText(code)
}

chrome.action.onClicked.addListener(tab => {
  chrome.scripting.executeScript({
    target: {tabId: tab.id},
    func: copyCode
  })
})
