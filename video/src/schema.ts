import { z } from 'zod';
export const R01Props = z.object({
  variante: z.enum(['dia20', 'logo']).default('dia20'),   // "VOLTO DIA 20." (com GO de 05/01) ou "VOLTO LOGO." (sem GO)
  semTexto: z.boolean().default(false),                    // QA do rosto: renderiza sem texto para medir onde o texto fica
  debug: z.boolean().default(false),                       // desenha área segura e caixa do rosto (só prévia de conferência)
  trilha: z.string().nullable().default(null),             // caminho dentro de public/, ou null (sem música)
});
export type R01PropsT = z.infer<typeof R01Props>;
