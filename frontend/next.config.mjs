/** @type {import('next').NextConfig} */
const nextConfig = {
	reactStrictMode: true,
	swcMinify: true,
	poweredByHeader: false,
	env: {
		API_URL: process.env.API_URL,
		API_VERSION: process.env.API_VERSION,
		WS_URL: process.env.WS_URL
	},
	images: {
		domains: ['https://www.minobrnauki.gov.ru/', 'localhost']
	},
	async rewrites() {
		return [
			{
				source: '/api/:path*',
				destination: 'http://localhost:8000/api/:path*'
			}
		]
	}
}

export default nextConfig;
