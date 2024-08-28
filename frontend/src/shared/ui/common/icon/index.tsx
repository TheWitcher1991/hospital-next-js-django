import { DetailedHTMLProps, FC, HTMLAttributes } from 'react'

interface IconProps
	extends DetailedHTMLProps<HTMLAttributes<HTMLElement>, HTMLElement> {
	label?: string
}

/**
 * Компонент для отображения mdi-icons иконки
 *
 * @param label имя иконки без "mdi mdi-"
 * @param ...rest
 * @site https://pictogrammers.com/library/mdi/
 */
export const Icon: FC<IconProps> = ({ label, ...rest }) => {
	return <i className={`mdi mdi-${label}`} {...rest}></i>
}
