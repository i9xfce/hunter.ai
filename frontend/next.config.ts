import type { NextConfig } from 'next'

const isGithubPages = process.env.GITHUB_PAGES === 'true'
const repository = process.env.GITHUB_REPOSITORY?.split('/')[1]
const basePath = isGithubPages && repository ? `/${repository}` : ''

const nextConfig: NextConfig = {
  output: 'export',
  basePath,
  assetPrefix: basePath,
  images: { unoptimized: true },
  trailingSlash: true,
}

export default nextConfig
