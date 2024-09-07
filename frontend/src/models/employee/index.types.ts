import { ICreateUser, IUpdateUser, IUser } from '@/models/account'
import { ICabinet } from '@/models/cabinet'
import { IPosition } from '@/models/position'

export interface IEmployee {
	id: number
	user: IUser
	cabinet: ICabinet
	position: IPosition
}

export interface IUpdateEmployee {
	user: IUpdateUser
	cabinet: number
	position: number
}

export interface ICreateEmployee {
	user: ICreateUser
	cabinet: number
	position: number
}
