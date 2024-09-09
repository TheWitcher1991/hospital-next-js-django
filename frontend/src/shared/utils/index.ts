import { toastr } from 'react-redux-toastr'

export const stringIncludes = (target: string, value: string) => {
	return target.toLowerCase().includes(value.toLowerCase())
}

export const requestErrorFactory = (error: any): string =>
	error.response && error.response.data
		? typeof error.response.data.message === 'object'
			? error.response.data.message[0]
			: error.response.data.message
		: error.message

export const toastError = (error: any, title: string = 'Error request') => {
	const message = requestErrorFactory(error)
	toastr.error(message, title)
	throw error
}
