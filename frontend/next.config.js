// next.config.js
export default  {
    reactStrictMode: true,
    productionBrowserSourceMaps: true,
    output: 'standalone',
    eslint: {
      dirs: ["pages"],
    },
    webpack: (config, { dev }) => {
      if (dev) {
        config.optimization.minimize = false;
      }
      return config;
    },
  };

