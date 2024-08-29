import { accountActions } from '@/models/account'
import { serviceTypeActions } from '@/models/service-type'
import { serviceActions } from '@/models/service'

export const AppActions = {
	...accountActions,
	...serviceActions,
	...serviceTypeActions,
}
