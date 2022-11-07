// This file is required by the index.html file and will
// be executed in the renderer process for that window.
// No Node.js APIs are available in this process because
// `nodeIntegration` is turned off. Use `preload.js` to
// selectively enable features needed in the rendering
// process.

const ipcRenderer = require("electron").ipcRenderer;
const remote = require("electron").remote;
const dialog = remote.require("electron").dialog;

// Get History.txt input path (local)
const txtBtn = document.querySelector(".txt-file-name-class");
txtBtn.addEventListener("click", (event) => {
  dialog
    .showOpenDialog({
      properties: ["openFile"],
      filters: [{ name: "History", extensions: ["txt"] }],
    })
    .then((result) => {
      console.log("[javascript] " + result.filePaths);

      // render result on id="txt-file-name-text"
      document.getElementById("history-path").innerHTML = result.filePaths;
    });
});

// Get History.txt output path (server)
const folderBtn = document.querySelector(".rom-folder-name-class");
folderBtn.addEventListener("click", (event) => {
  dialog
    .showOpenDialog({
      properties: ["openDirectory"],
      defaultPath: "\\\\Binary",
    })
    .then((result) => {
      console.log("[javascript] " + result.filePaths);

      //render result on id="rom-folder-name-text"
      document.getElementById("rom-path").innerHTML = result.filePaths + "\\";
    });
});

// Send data to python and close window
const btn = document.querySelector(".release-btn-class");
if (btn) {
  btn.addEventListener("click", (event) => {
    document.getElementById("release-load-icon-id").classList =
      "svg-inline--fa fa-circle-notch fa-w-16 fa-spin";
    document.getElementById("release-button-id").setAttribute("disabled", true);
    document.getElementById("release-button-id").style.backgroundColor =
      "#848884";
    document.getElementById("release-status-id").innerText = "Loading";

    var historyPath = document.getElementById("history-path").textContent;
    var romPath = document.getElementById("rom-path").textContent;
    var isEmail = document.querySelector("#isEmail").checked.toString();
    var isClipboard = document.querySelector("#isClipboard").checked.toString();
    var isClose = document.querySelector("#isClose").checked.toString();

    // Can check log by toggling devMode via Ctrl+Shift+I
    console.log("[javascript] history Path: " + historyPath);
    console.log("[javascript] rom Path: " + romPath);
    console.log("[javascript] isEmail: " + isEmail);
    console.log("[javascript] isClipboard: " + isClipboard);
    console.log("[javascript] isClose: " + isClose);

    var python = require("child_process").spawn(
      "resources\\app\\dist\\main_py.exe",
      [historyPath, romPath, isEmail, isClipboard]
    );

    python.stdout.on("data", function (data) {
      const electronAnchor = new RegExp(/^Status_Anchor:/);
      document.getElementById("release-load-icon-id").classList =
        "svg-inline--fa fa-circle-notch fa-w-16 fa-spin";
      if (data.toString().match(electronAnchor)) {
        document.getElementById("release-status-id").innerText = data
          .toString()
          .split("Status_Anchor:")[1]
          .trim();
      }

      console.log(data.toString());
    });

    python.stderr.on("data", (data) => {
      // Turn Relaese Button style back
      setReleaseBtnBack();

      console.log(`stderr: ${data}`);

      const pythonException = new RegExp(/release_exp:/);
      if (data.toString().match(pythonException)) {
        const options = {
          type: "warning",
          buttons: ["Got it"],
          title: "Warning",
          message: data.toString().split("release_exp:")[1].trim(),
        };

        dialog.showMessageBox(null, options, (response, checkboxChecked) => {
          console.log("[javascript] " + response);
          console.log("[javascript] " + checkboxChecked);
        });
      }
    });

    python.on("close", (code) => {
      console.log(`child process exited with code ${code}`);

      document.getElementById("release-status-id").innerText = "Finish";

      // Turn Relaese Button style back
      setReleaseBtnBack();

      // Here we close this app
      if (!code) {
        if (isClose == "true") {
          ipcRenderer.send("close-main-window");
        }
      }
    });

    function setReleaseBtnBack() {
      document.getElementById("release-load-icon-id").classList =
        "svg-inline--fa fa-upload fa-w-16 fa-lg";
      document.getElementById("release-status-id").innerText = "Release";
      document.getElementById("release-button-id").removeAttribute("disabled");
      document.getElementById("release-button-id").style.backgroundColor =
        "#2196F3";
    }
  });
}
