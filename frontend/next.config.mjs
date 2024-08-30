/** @type {import('next').NextConfig} */
const nextConfig = {
	reactStrictMode: true,
	swcMinify: true,
	poweredByHeader: false,
	env: {

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
