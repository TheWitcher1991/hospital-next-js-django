import { IAgreement } from '@/models/agreement'

export interface IBaseTalon {
	result: string
}

export interface ITalon extends IBaseTalon {
	id: number
	agreement: IAgreement
}

export interface ICreateTalon extends IBaseTalon {
	agreement: number
}

export type IUpdateTalon = IBaseTalon
