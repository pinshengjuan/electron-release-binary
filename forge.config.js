module.exports = {
  packagerConfig: {
    icon: "ico/icons/win/icon.ico",
    win32metadata: {
      "requested-execution-level": "requireAdministrator",
    },
  },
  makers: [
    {
      name: "@electron-forge/maker-wix",
      config: {
        name: "Release Binary",
        exe: "Release Binary",
        features: {
          autoUpdate: true,
        },
        arch: "x64",
      },
    },
    {
      name: "@electron-forge/maker-zip",
      platforms: "darwin",
    },
    {
      name: "@electron-forge/maker-deb",
      config: {},
    },
    {
      name: "@electron-forge/maker-rpm",
      config: {},
    },
  ],
};
