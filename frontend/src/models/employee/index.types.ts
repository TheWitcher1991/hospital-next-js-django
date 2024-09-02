import { IUpdateUser, IUser } from '@/models/account'
import { ICabinet } from '@/models/cabinet'
import { IPosition } from '@/models/position'

export interface IEmployee {
	user: IUser
	cabinet: ICabinet
	position: IPosition
}

export interface IUpdateEmployee {
	user: IUpdateUser
	cabinet: number
	position: number
}
