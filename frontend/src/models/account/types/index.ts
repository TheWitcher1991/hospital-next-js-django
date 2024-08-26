import {UserRole} from "@/models/account/enums";

export interface AccountState {
    id: number
    role: UserRole
    access_token: string
    isAuthenticated: boolean
}
