import { UserRole } from '@/models/account/index.enums'

export interface AccountState {
	id: number
	role: UserRole
	access_token: string
	isAuthenticated: boolean
}
