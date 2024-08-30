import { FC, PropsWithChildren } from 'react'
import ReduxToastr from 'react-redux-toastr'

const WithToastr: FC<PropsWithChildren> = ({ children }) => {
	return (
		<>
			{children}
			<ReduxToastr
				newestOnTop={false}
				preventDuplicates
				progressBar
				closeOnToastrClick
				timeout={3000}
				transitionIn='fadeIn'
				transitionOut='fadeOut'
				getState={state => state.toastr}
			/>
		</>
	)
}

export default WithToastr
