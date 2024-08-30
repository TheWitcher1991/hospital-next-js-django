import type { AppProps } from 'next/app'
import Header from '@/widgets/header'
import Footer from '@/widgets/footer'
import WithProviders from '@/providers'
import { Root } from '@/shared/ui'
import '@mdi/font/css/materialdesignicons.css'
import 'react-redux-toastr/lib/css/react-redux-toastr.min.css'
import '@/shared/css/global.css'

export default function MyApp({ Component, pageProps }: AppProps) {
	return (
		<WithProviders>
			<Root>
				<Header />
				<Component {...pageProps} />
				<Footer />
			</Root>
		</WithProviders>
	)
}
