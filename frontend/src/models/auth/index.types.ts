export interface ILogin {
	email: string
	password: string
}

export interface ILoginReturn {
	access_token: string
	expires: string
	token_type: 'Bearer'
}

export interface AuthState {
	isLoading: boolean
}
