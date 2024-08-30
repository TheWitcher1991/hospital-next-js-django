import { FC, PropsWithChildren } from 'react'
import WithProgressBar from '@/providers/with-progress-bar'
import WithStore from '@/providers/with-store'
import WithPersist from '@/providers/with-persist'
import WithToastr from '@/providers/with-toastr'

const WithProviders: FC<PropsWithChildren> = ({ children }) => {
	return (
		<WithProgressBar>
			<WithStore>
				<WithPersist>
					<WithToastr>{children}</WithToastr>
				</WithPersist>
			</WithStore>
		</WithProgressBar>
	)
}

export default WithProviders
