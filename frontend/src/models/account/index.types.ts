import { UserFloor, UserRole } from '@/models/account/index.enums'

export interface IBaseUser {
	email: string
	first_name: string
	last_name: string
	patronymic: string
	date: string
	age: number
	gender: UserFloor
	role: UserRole
}

export interface IUser extends IBaseUser {
	id: number
	is_online: boolean
	last_ip: Nullable<string>
	last_online: Nullable<string>
	date_joined: string
}

export type IUpdateUser = Omit<IBaseUser, 'role'>

export type ICreateUser = IBaseUser

export interface AccountState {
	id: number
	role: UserRole
	access_token: string
	isAuthenticated: boolean
}
