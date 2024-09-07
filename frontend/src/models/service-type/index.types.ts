export interface IServiceType {
	id: number
	name: string
	ico: string
}

export interface ServiceTypeState {
	count: number
	isLoading: boolean
	isError: boolean
	types: IServiceType[]
}
