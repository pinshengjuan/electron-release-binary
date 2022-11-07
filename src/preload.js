// All of the Node.js APIs are available in the preload process.
// It has the same sandbox as a Chrome extension.
const ipcRenderer = require("electron").ipcRenderer;
const remote = require("electron").remote;

window.addEventListener("DOMContentLoaded", () => {
  // const replaceText = (selector, text) => {
  //   const element = document.getElementById(selector)
  //   if (element) element.innerText = text
  // }

  // for (const type of ['chrome', 'node', 'electron']) {
  //   replaceText(`${type}-version`, process.versions[type])
  // }
  global.sharedObject = { prop1: process.argv };
  const remote = require("electron").remote;

  // Get all arguments from system
  var args = remote.getGlobal("sharedObject").prop1;

  // Get second argument
  var arg1 = args.toString().split(",")[1];
  console.log("[javascript] args: " + args);

  // If the argument endup with .txt then we change the text
  if (arg1.match(RegExp(/.txt$/))) {
    console.log("[javascript] ready to change history path text");
    document.getElementById("history-path").innerText = arg1;
  }
});
