import { FC, ReactNode } from 'react'
import styles from './index.module.css'

interface LabelProps extends OmitClassName<DetailedLabelProps> {
	children?: ReactNode
	required?: boolean
}

export const Label: FC<LabelProps> = ({
	children,
	required,
	htmlFor,
	...rest
}) => (
	<label className={`${styles.label__field}`} {...rest}>
		{children} {required && <span>*</span>}
	</label>
)
