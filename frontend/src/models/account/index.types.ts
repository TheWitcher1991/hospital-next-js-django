import { UserFloor, UserRole } from '@/models/account/index.enums'

export interface IBaseUser {
	email: string
	first_name: string
	last_name: string
	patronymic: string
	age: number
	date: string
	date_joined: string
	gender: UserFloor
	role: UserRole
}

export interface IUser extends IBaseUser {
	id: number
	is_online: boolean
	last_ip: Nullable<string>
	last_online: Nullable<string>
}

export type IUpdateUser = IBaseUser

export interface AccountState {
	id: number
	role: UserRole
	access_token: string
	isAuthenticated: boolean
}
