export interface IServiceType {
	name: string
	ico: string
}

export interface ServiceTypeState {
	count: number
	isLoading: boolean
	isError: boolean
	types: IServiceType[]
}
