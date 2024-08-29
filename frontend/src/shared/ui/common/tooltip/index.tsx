'use client'

import {
	FC,
	PropsWithChildren,
	useCallback,
	useEffect,
	useRef,
	useState,
} from 'react'
import styles from './index.module.css'

interface TooltipProps extends PropsWithChildren {
	label?: string
}

export const Tooltip: FC<TooltipProps> = ({ label, children }) => {
	const [visible, setVisible] = useState(false)
	const [left, setLeft] = useState(0)
	const containerRef = useRef<Nullable<HTMLDivElement>>(null)
	const tooltipRef = useRef<Nullable<HTMLDivElement>>(null)

	const handleMouseEnter = useCallback(() => {
		setVisible((prev) => !prev)
	}, [])

	const handleMouseLeave = useCallback(() => {
		setVisible((prev) => !prev)
	}, [])

	useEffect(() => {
		if (visible && containerRef.current && tooltipRef.current) {
			const containerWidth = containerRef.current.offsetWidth
			const tooltipWidth = tooltipRef.current.offsetWidth
			setLeft((containerWidth - tooltipWidth) / 2)
		}
	}, [visible])

	if (!label) return children

	return (
		<div
			ref={containerRef}
			onMouseEnter={handleMouseEnter}
			onMouseLeave={handleMouseLeave}
			className={styles.tooltip}
		>
			{children}
			<div
				ref={tooltipRef}
				role={'tooltip'}
				className={styles.tooltip__label}
				style={{
					opacity: visible ? 1 : 0,
					pointerEvents: visible ? 'auto' : 'none',
					left: `${left}px`,
				}}
			>
				{label}
			</div>
		</div>
	)
}
