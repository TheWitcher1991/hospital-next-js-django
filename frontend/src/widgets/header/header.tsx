import { FC } from 'react'
import { Button, Container, Icon, Logo } from '@/shared/ui'
import styles from './header.module.css'

export const Header: FC = () => {
	return (
		<header className={styles.header}>
			<Container>
				<nav className={styles.header__nav}>
					<Logo />
					<Button>
						<Icon label={'login'} />
						Авторизация
					</Button>
				</nav>
			</Container>
		</header>
	)
}
