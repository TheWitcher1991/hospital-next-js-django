import { accountActions } from '@/models/account'
import { serviceTypeActions } from '@/models/service-type'
import { serviceActions } from '@/models/service'
import { authActions } from '@/models/auth'

export const AppActions = {
	...accountActions,
	...serviceActions,
	...serviceTypeActions,
	...authActions,
}
