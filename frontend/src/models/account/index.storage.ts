import { AccountState } from '@/models/account/index.types'

export const accountStorageKey = 'accountState'

export const loadStateFromLocalStorage = (): Nullable<
	Partial<AccountState>
> => {
	try {
		if (typeof window === 'undefined') return { isAuthenticated: false }

		const serializedState: Nullable<string> =
			localStorage.getItem(accountStorageKey)
		if (!serializedState) {
			return { isAuthenticated: false }
		}
		return JSON.parse(serializedState)
	} catch (e) {
		console.warn('Ошибка при загрузке состояния из localStorage:', e)
		return { isAuthenticated: false }
	}
}

export const saveStateToLocalStorage = (
	state: Nullable<Partial<AccountState>>,
) => {
	try {
		if (typeof window === 'undefined') return

		const serializedState = JSON.stringify(state)
		localStorage.setItem(accountStorageKey, serializedState)
	} catch (e) {
		console.warn('Ошибка при сохранении состояния в localStorage:', e)
	}
}
