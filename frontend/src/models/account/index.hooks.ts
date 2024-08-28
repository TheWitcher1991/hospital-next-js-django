import { useAppSelector } from '@/hooks'

export const useCheckAuth = () => {
	const { isAuthenticated, role } = useAppSelector((state) => state.account)

	return {
		role,
		isAuthenticated,
	}
}
