/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',
  trailingSlash: true,
  images: {
    unoptimized: true
  },
  // Prevent Next.js from trying to statically generate routes that don't exist
  experimental: {
    // Disable static generation for routes that cause issues
    serverComponentsExternalPackages: [],
  }
}

module.exports = nextConfig