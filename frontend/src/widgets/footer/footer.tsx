import { FC } from 'react'
import { Container, Logo } from '@/shared/ui'
import Image from 'next/image'
import styles from './Footer.module.css'

export const Footer: FC = () => {
	return (
		<footer className={styles.footer}>
			<Container>
				<div className={styles.footer__container}>
					<div className={styles.footer__img}>
						<Logo />
						<Image
							width={160}
							height={160}
							src={
								'https://www.minobrnauki.gov.ru/local/templates/minobr/images/dest/logo-mobile.svg'
							}
							alt={'Minobrnauki'}
						/>
					</div>
				</div>
			</Container>
		</footer>
	)
}
