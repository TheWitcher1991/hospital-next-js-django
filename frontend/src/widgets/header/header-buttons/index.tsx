'use client'

import { FC } from 'react'
import { Button, Flex, Icon } from '@/shared/ui'
import { useCheckAuth } from '@/models/account'

export const HeaderButtons: FC = () => {
	const { isAuthenticated } = useCheckAuth()

	return (
		<>
			{isAuthenticated && <Button variant={'black'}>Кабинет</Button>}
			{!isAuthenticated && (
				<Flex gap={16}>
					<Button variant={'secondary'}>
						<Icon label={'account-plus'} />
						Регистрация
					</Button>
					<Button>
						<Icon label={'login'} />
						Войти
					</Button>
				</Flex>
			)}
		</>
	)
}
