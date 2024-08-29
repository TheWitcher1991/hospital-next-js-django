import { FC, PropsWithChildren } from 'react'
import WithStore from '@/providers/with-store'

const WithProviders: FC<PropsWithChildren> = ({ children }) => {
	return <WithStore>{children}</WithStore>
}

export default WithProviders
